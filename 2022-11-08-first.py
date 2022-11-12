import os, io, __pypy__

class FastIO:
	def __init__(self):
		self.r = io.BytesIO(os.read(0, os.fstat(0).st_size)).read()
		self.w = __pypy__.builders.StringBuilder()
		self.i = 0
	def Flush(self): os.write(1, self.w.build().encode())
	def ReadInt(self):
		ret = 0
		while self.r[self.i] & 16: ret = 10 * ret + (self.r[self.i] & 15); self.i += 1
		self.i += 1
		return ret
	def Write(self, x): self.w.append(x)

IO = FastIO()
n = IO.ReadInt()
IO.Write('\n'.join(map(str, [IO.ReadInt() + IO.ReadInt() for _ in range(n)])));
IO.Flush()