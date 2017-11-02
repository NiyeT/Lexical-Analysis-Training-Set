class venn:

	def groupTwo(self,matrix):
		group=[]
		for index in range(len(matrix)):
			pair=[]
			if(index!=len(matrix)-1):			
				current=matrix[index]
				adjacent=matrix[index+1]
				pair.append(current)
				pair.append(adjacent)
			if(pair):
				group.append(pair)
		return group

	def groupN(self,matrix):
		return False

	def matrixComp(self,matrix1,matrix2):
		if(len(matrix1)!=len(matrix2)):
			return False
		for val in range(len(matrix1)):
			try:
				matrix1[val].lower()
				matrix2[val].lower()						
			except:
				pass
		length=len(matrix1)
		for group in range(length):
			if(matrix1[group]==matrix2[group]):
				pass
			else:
				return False		
		return True


	def factorial(self,matrix):
		product=[]
		n=len(matrix)
		for group in range(n):
			temp=[]
			current=matrix[group]
			start=(group + 1)
			iterate=n-start
			for pair in range(iterate):
				touch=matrix[pair+start]
				print current
				print touch
				if(self.matrixComp(current,touch)):
					print True
				else:
					print False
				print '\n'

venn=venn()
