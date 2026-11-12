import json,os,urllib.request as U
M=[0,100,320,330,500,900,0]
WA=[0,3,10,8,4,5,0]
B=[0]*128;K=[0,0];BUD=4e4;H={};V=[]
CM={0:2,7:1,112:8,119:4}
def ak(s,c):
 for d,p in((-15*c,1),(-17*c,1),(14,2),(18,2),(31,2),(33,2),(-14,2),(-18,2),(-31,2),(-33,2)):
  q=s+d
  if not q&136 and B[q]==p*c:return 1
 for d in(1,-1,16,-16,15,-15,17,-17):
  q=s+d
  while not q&136 and not B[q]:q+=d
  if not q&136:
   p=B[q]*c
   if p==5 or p==6 and q==s+d or p==4-(abs(d)not in(1,16)):return 1
 return 0
def gn(cp):
 ms=[]
 for i,p in enumerate(B):
  if p*S<=0:continue
  a=abs(p)
  if a==1:
   d=16*S
   for t in(i+d,i+d-1,i+d+1):
    if t&136 or t==i+d and B[t]or cp and t==i+d and(t>>4)%7 or t!=i+d and B[t]*S>=0 and t!=Y:continue
    for q in((2,3,4,5)if not(t>>4)%7 else(0,)):ms.append(i|t<<7|q<<14)
    if not cp and t==i+d and(i>>4)==1+5*(S<0)and not B[t+d]:ms.append(i|(t+d)<<7)
  else:
   sl=2<a<6
   for o in((14,18,31,33),(15,17),(1,16),(1,15,16,17))[min(a-2,3)]:
    for e in(o,-o):
     t=i+e
     while not t&136:
      if B[t]*S>0:break
      if not cp or B[t]:ms.append(i|t<<7)
      if B[t]or not sl:break
      t+=e
   if a==6 and not cp:
    k=4 if S>0 else 116
    for g in(1,-1):
     if i==k and C>>((S<0)*2+(g<0))&1 and not B[k+g]and not B[k+2*g]and(g>0 or not B[k+3*g])and not any(ak(k+j*g,-S)for j in(0,1,2)):ms.append(i|(k+2*g)<<7)
 return[m for m in ms if(mk(m),not ak(K[S>0],S),um(m))[1]]
def mk(m):
 global S,C,Y
 f=m&127;t=m>>7&127;q=m>>14;Z=B[f];c=B[t];cs=t
 if abs(Z)==1 and t==Y and not c:cs=t-16*S;B[cs]=0;c=-S
 V.append((c,cs,C,Y));B[t]=Z;B[f]=0
 if abs(Z)==1:
  if q:B[t]=q*S
  Y=f+16*S if abs(t-f)==32 else-1
 else:Y=-1
 if abs(Z)==6:
  K[S<0]=t;C&=~(3<<2*(S<0))
  if abs(t-f)==2:o=1 if t>f else-1;r=f+3*o-(o<0);B[f+o]=B[r];B[r]=0
 for x in(f,t):C&=~CM.get(x,0)
 S=-S
def um(m):
 global S,C,Y
 S=-S;f=m&127;t=m>>7&127;q=m>>14
 c,cs,C,Y=V.pop();Z=B[t]
 B[f]=S if q else Z;B[t]=0
 if c:B[cs]=c
 if abs(Z)==6:
  K[S<0]=f
  if abs(t-f)==2:o=1 if t>f else-1;r=f+3*o-(o<0);B[r]=B[f+o];B[f+o]=0
def ev():
 s=0
 for i,p in enumerate(B):
  if p:
   a=abs(p);f=i&7;r=i>>4
   v=M[a]+(min(f,7-f)+min(r,7-r))*WA[a]
   if a==1:v+=((r-1)if p>0 else(6-r))*4
   s+=v if p>0 else-v
 return S*s+10
def od(ms,hm):return sorted(ms,key=lambda m:-((m>>14)*1000+(m==hm)*1000000+((10000+abs(v)*10)if(v:=B[m>>7&127])else 0)))
def sr(a,b,d,pl):
 global N;N+=1
 if N>BUD:return None
 if d<-6:return ev()
 ck=ak(K[S<0],-S);q=d<=0
 if q and not ck:
  s=ev()
  if s>=b:return b
  if s>a:a=s
 ms=gn(q and not ck)
 if not ms:return -99999+pl if ck else a if q else 0
 h=(tuple(B),S,C,Y);e=H.get(h);hm=e[2]if e else 0
 if e and e[0]>=d:return e[1]
 bo=a;bm=0
 for m in od(ms,hm):
  mk(m);r=sr(-b,-a,d-1,pl+1);um(m)
  if r is None:return None
  s=-r
  if s>=b:return b
  if s>bo:bo=s;bm=m
 if bm and not q:H[h]=(d,bo,bm)
 return bo
def ch():
 global N;N=0
 H.clear()
 ms=gn(False)
 if len(ms)==1:return ms[0]
 best=ms[0]
 for d in range(1,40):
  bo=-1e6;sc=[]
  for m in od(ms,best):
   mk(m);r=sr(-1e6,1e6,d-1,1);um(m)
   if r is None:return best
   s=-r;sc.append((s,m))
   if s>bo:bo=s;bm=m
  best=bm
  if d==1:ms=[m for s,m in sorted(sc)[-6:]]
 return best
def su(mv):
 global S,C,Y
 B[:]=[0]*128
 for i,v in enumerate((4,2,3,5,6,3,2,4)):B[i]=v;B[i+112]=-v;B[i+16]=1;B[i+96]=-1
 K[:]=4,116;S=1;C=15;Y=-1
 for m in mv:mk((ord(m[0])-97+(ord(m[1])-49)*16)|(ord(m[2])-97+(ord(m[3])-49)*16)<<7|(m[4:]and'nbrq'.find(m[4])+2 or 0)<<14)
def uc(m):return chr(97+(m&7))+str((m>>4&7)+1)+chr(97+(m>>7&7))+str((m>>11&7)+1)+(''if not m>>14 else'nbrq'[(m>>14)-2])
def cl(p,o):
 for _ in'12':
  try:return json.load(U.urlopen(U.Request(E+p,data=json.dumps(o).encode()),timeout=9))
  except U.HTTPError:raise
  except:
   if _=='2':raise
E=os.getenv('MAKEFUN_ENV_URL','').rstrip('/')
def main():
 while 1:
  g=cl('/game',{})
  if g['status']=='done':return
  while g['status']=='your_move':
   try:su(g['moves']);mv=uc(ch())
   except:mv=''
   for mv in[mv]+[x for x in g['legal_moves'] if x!=mv]:
    try:g=cl('/move',{'game':g['game'],'move':mv});break
    except:pass
   else:return
if E:main()
