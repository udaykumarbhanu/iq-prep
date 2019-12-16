def topNcompetitors_func(numCompetitors, topNcompetitors, competitors, numReviews, reviews):
	wordcount_table = dict()
	reviews = [review.lower() for review in reviews]

	for review in reviews:
		for competitor in competitors:
			if competitor in review:
				wordcount_table[competitor] = wordcount_table.get(competitor, 0)  + 1

	sorted_wordcount_table = list(sorted(wordcount_table.items(), key=lambda x: x[1], reverse=True))

	if topNcompetitors < numCompetitors:
		return [k for k, val in sorted_wordcount_table[: topNcompetitors]]

	else:
		return [k for k, val in sorted_wordcount_table]


if __name__ == '__main__':
	numCompetitors = 6
	topNcompetitors = 2 
	competitors = ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular'] 
	numReviews = 6
	reviews = ['newshop is providing good services in the city;everyone should use newshop',
			'best services by newshop','fashionbeats has great services in the city',
			'I am proud to have fashionbeats', 'mymarket has awesome services',
			'Thanks Newshop for the quick delivery.']

	print topNcompetitors_func(numCompetitors, topNcompetitors, competitors, numReviews, reviews)