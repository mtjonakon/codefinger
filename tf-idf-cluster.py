'''Path 1: clustering using tf-idf'''

#get top n tfidf values in row and return them with corresponding feature names
def top_tfidf_feats(row,features,top_n=75):
	topn_ids = np.argsort(row)[::-1][:top_n]
	top_feats = [(features[i], row[i]) for i in topn_ids]
	df = pd.DataFrame(top_feats)
	df.columns = ['feature', 'score']
	return df 

def top_feats_in_doc(tfidf_matrix, features, row_id, top_n=75):
	row = np.squeeze(tfidf_matrix[row_id].toarray())
	return top_tfidf_feats(row,features,top_n)

#map rows to texts
print 'doc_name : row combinations'
print arrange.items()
print len(arrange)

#create a list of top 25 terms per document
text_tokens_idf = []
for i,j in zip(sorted(arrange, key=arrange.__getitem__),range(tfs.shape[0])): 
	slist = []
	m = top_feats_in_doc(tfs,feature_names,j).set_index('feature').to_dict()
	m = m['score']
	slist.append(i)
	slist.append(m)
	text_tokens_idf.append(slist)
