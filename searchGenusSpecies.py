def search(x_, y_, width, dic, bottom_data) :
	x = int(round(x_))
	dic_num = len(dic)

	ncols =  len(dic[1]['rate'])

	if x - width/2 < x_ and x_ < x + width/2 and x_ < ncols -1 - width/2:
		if y_ <= bottom_data[dic_num][x-1] :
			y_dic = bts(y_, 1, dic_num, x-1, dic, bottom_data)
			return x-1, y_dic
		else :#out of y-aix data 
			return None, None
	else : #out of x-aix data 
		return None, None
   
def bts(data, l, r, x, dic, bottom_data) :
	d = (r-l)/2
	l_data = bottom_data[l][x]
	r_data = bottom_data[r][x]
	m_data = bottom_data[l+d][x]

	if d < 1 :
		return dic[r]
	
	if data <= l_data :
		return dic[l]
	elif l_data < data and data<=m_data :
		return bts(data, l, l+d, x, dic, bottom_data)
	elif m_data < data and data <=r_data :
		return bts(data, l+d,r, x, dic, bottom_data)


