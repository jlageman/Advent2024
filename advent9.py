dat = [int(x) for x in open('input9.txt').read().splitlines()[0]]

# part 1 + 2
class Disk:
    def __init__(self, dat):
        self.disk = []
        self.files = []
        self.space = []
        self.space_start = {}
        self.file_start = {}
        for i, d in enumerate(dat):
            if i%2!=0:
                self.space_start[i//2] = len(self.disk)
                self.space.append(d)
                for _ in range(d):
                    self.disk.append('.')
            else:
                self.file_start[i//2] = len(self.disk)
                self.files.append(d)
                for _ in range(d):
                    self.disk.append(i//2)
    
    def compact_count(self):
        cdisk = [x for x in self.disk]
        ans = 0
        for i, d in enumerate(cdisk):
            if d=='.':
                block = '.'
                while block=='.':
                    block = cdisk.pop(-1)
                ans += (i*block)
            else:
                ans += (i*d)
        return ans
    
    def compact_full_count(self):
        space = [x for x in self.space]
        # compact files
        for i, f in enumerate(reversed(self.files)):
            filenum = len(self.files)-1-i
            search = space if i==0 else space[:-i]
            for ii, s in enumerate(search):
                if s >= f:
                    # adjust space
                    space[ii] = s-f
                    self.file_start[filenum] = self.space_start[ii]
                    self.space_start[ii] = self.space_start[ii]+f
                    break
        self.adj_space = space
        # compute checksum
        ans = 0
        for i, f in enumerate(self.files):
            for ii in range(f):
                ans += (i * (self.file_start[i]+ii))
        return ans
        
d = Disk(dat)
ans = d.compact_count()
ans2 = d.compact_full_count()