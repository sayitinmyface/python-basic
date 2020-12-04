# # # # # _ = [1,2,3]
# # # # b = ('1','2','3')
# # # # # c = {'a','b','c'}

# # # # # for d,e,f in zip(_,b,c):
# # # # #     print('a=',d,'b=',e,'c=',f)
# # # # # b[0] = 123213
# # # # # print(b[0])

# # # # # def sum(first,second):
# # # # #     result = first+second
# # # # #     return result,first,second

# # # # # first , second = input('input?').split(',')
# # # # # result,first,second = sum(int(first),int(second))

# # # # # print(f'{result},{first},{second}')


# # # # def return_tuple(arg,*arg_tuple):
# # # #     print(arg)
# # # #     for var in arg_tuple:
# # # #         print('var : ',var)
# # # #     return arg_tuple

# # # # return_tuple(10)
# # # # print(return_tuple(1,2,3,4,4,1,1,1,1,))

def aaaa(the_list,level=1):
    for f_var in the_list:
        if isinstance(f_var,list):
            aaaa(f_var,level+1)
            # print(level)
        else:
            for ff_var in range(level):
                print('*',end='')
            print(f_var)

m = [1,2,['kk','jj','ii'],3,4,['a','b','c','d','e']]
aaaa(m)

# # def aa(*bb,**cc):
# #     print('1',bb,type(bb))
# #     print('2',cc,type(cc))

# # aa(12,3,342,343,2,a='a')    

# # ii = [1,2,3,4]
# # jj = {'a':'A'}
# # aa(ii,jj,a='B')

# # sum = lambda arg1,arg2:arg1+arg2
# # print('value = ',sum(1,2))

# nums = [1,2,3]
# def is_one(x):
#     return x>1
# # mmm = filter(is_one,range(90))    
# print(type(mmm))
# print(list(mmm))
# mmm = filter(lambda x: x>1,range(5))
# print(list(range(3)))
# print(type(mmm))
# print(list(mmm))
