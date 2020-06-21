import search
import time
import numpy as np
mixed_seqs = ['CACADLGAYPDKLIF','CACDALLAYTDKLIF','CACDAVGDTLDKLIF','CACDDVTEVEGDKLIF','CACDFISPSNWGIQSGRNTDKLIF','CACDILLGDTADKLIF','CACDIVLSGGLDTRQMFF','CACDLLLRQSSTDKLIF','CACDNLSETTDKLIF','CACDPLGTDKLIF','CACDPMGGSGGLSWDTRQMFF','CACDPVLGDTRLTDKLIF','CACDPVQGYSGQNRAYTDKLIF','CACDSILGDTLYTDKLIF','CACDSLTSHTGGFGPDKLIF','CACDSTGDLSSWDTRQMFF','CACDSVESRNVLGDPTTDKLIF','CACDSVLSRDLGDSELIF','CACDTAAGGYASSWDTRQMFF','CACDTAPHGGRTWDTRQMFF','CACDTGGYVNWDTRQMFF','CACDTGRLLGDTADTRQMFF','CACDTIRGFSSWDTRQMFF','CACDTIVAPALDKLIF','CACDTLFLGEDTPTDKLIF','CACDTLGDLSLTAQLFF','CACDTLGDPPHTDKLIF','CACDTLGDYTQSDKLIF','CACDTLGGYPWDTRQMFF','CACDTLGKTDKLIF','CACDTLPLKTGGPLYTDKLIF','CACDTLRLGDPLNTDKLIF','CACDTVALGDTESSWDTRQMFF','CACDTVGAVLGDPKGTDKLIF','CACDTVGDGPDTDKLIF','CACDTVGDTADKLIF','CACDTVGDTHSWDTRQMFF','CACDTVGGSTDKLIF','CACDTVGIPPDKLIF','CACDTVGYGEGDTDKLIF','CACDTVISSNRRGGDKLIF','CACDTVPPGDTGTDKLIF','CACDTVRFTGGYENTDKLIF','CACDYVLGAEDKLIF','CACEGILKSEPLGIDKLIF','CACEMLGHPPGDKLIF','CACVSLDLSYTDKLIF','CALGEIAFRSRTGGPPYTDKLIF','CALGTAYFLRDPGADKLIF','CAVKVPLTSSPREGPTVLHDKLIF']

reps = 1000
max_lvdif = 4
start = time.time()
index_store = dict()
for i in range(len(mixed_seqs)):	
	ms = list(mixed_seqs)
	s = ms.pop(i)
	svec = reps*ms
	n = len(svec)
	mv = search.lv_rect(s = s, svec = svec, n = n)
	dists = np.asarray(mv)
	ind_nn = np.argwhere(dists < max_lvdif).flatten()
	index_store[s] = ind_nn
print(index_store.keys())
end =  time.time()
cy_time = end - start


network = [(k, svec[i]) for k,v in index_store.items() for i in v]
for node1, node2 in network[1:100]:
	print(f"{node1}\n{node2}")
	print("")

print(f"{round(100*len(network)/(len(ms)*len(svec)),2)}% i,e., Network/Total Comparisons")
print("Search time (Cython) = {}".format(cy_time))