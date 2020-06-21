import search
import time
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix

mixed_seqs = ['CACADLGAYPDKLIF','CACDALLAYTDKLIF','CACDAVGDTLDKLIF','CACDDVTEVEGDKLIF','CACDFISPSNWGIQSGRNTDKLIF','CACDILLGDTADKLIF','CACDIVLSGGLDTRQMFF','CACDLLLRQSSTDKLIF','CACDNLSETTDKLIF','CACDPLGTDKLIF','CACDPMGGSGGLSWDTRQMFF','CACDPVLGDTRLTDKLIF','CACDPVQGYSGQNRAYTDKLIF','CACDSILGDTLYTDKLIF','CACDSLTSHTGGFGPDKLIF','CACDSTGDLSSWDTRQMFF','CACDSVESRNVLGDPTTDKLIF','CACDSVLSRDLGDSELIF','CACDTAAGGYASSWDTRQMFF','CACDTAPHGGRTWDTRQMFF','CACDTGGYVNWDTRQMFF','CACDTGRLLGDTADTRQMFF','CACDTIRGFSSWDTRQMFF','CACDTIVAPALDKLIF','CACDTLFLGEDTPTDKLIF','CACDTLGDLSLTAQLFF','CACDTLGDPPHTDKLIF','CACDTLGDYTQSDKLIF','CACDTLGGYPWDTRQMFF','CACDTLGKTDKLIF','CACDTLPLKTGGPLYTDKLIF','CACDTLRLGDPLNTDKLIF','CACDTVALGDTESSWDTRQMFF','CACDTVGAVLGDPKGTDKLIF','CACDTVGDGPDTDKLIF','CACDTVGDTADKLIF','CACDTVGDTHSWDTRQMFF','CACDTVGGSTDKLIF','CACDTVGIPPDKLIF','CACDTVGYGEGDTDKLIF','CACDTVISSNRRGGDKLIF','CACDTVPPGDTGTDKLIF','CACDTVRFTGGYENTDKLIF','CACDYVLGAEDKLIF','CACEGILKSEPLGIDKLIF','CACEMLGHPPGDKLIF','CACVSLDLSYTDKLIF','CALGEIAFRSRTGGPPYTDKLIF','CALGTAYFLRDPGADKLIF','CAVKVPLTSSPREGPTVLHDKLIF']

reps = 1000
max_lvdif = 4
start = time.time()
index_store = dict()
indices = list()
ms = list(mixed_seqs)
svec = reps*ms
n = len(svec)

for i in range(len(mixed_seqs)):	
	s = ms[i]
	mv = search.lv_rect(s = s, svec = svec, n = n)
	dists = np.asarray(mv)
	ind_nn = np.argwhere(dists < max_lvdif).flatten()
	index_store[s] = ind_nn
	for j in ind_nn:
		indices.append( (i,j) )

# Convert the data into a sparse matrix format
row = list()
col = list()
for i,j in indices:
	row.append(i)
	col.append(j)
row = np.array(row)
col = np.array(col)
data = np.ones(row.shape[0])
x = coo_matrix((data, (row, col)), shape = (len(ms), len(svec)))
print(x.shape)
print(x)


#network = [(k, svec[i]) for k,v in index_store.items() for i in v]
# for node1, node2 in network[1:100]:
# 	print(f"{node1}\n{node2}")
# 	print("")
#print(f"{round(100*len(network)/(len(ms)*len(svec)),2)}% i,e., Network/Total Comparisons")
end =  time.time()
cy_time = end - start
print("Search time (Cython) = {}".format(cy_time))
