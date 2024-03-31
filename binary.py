from stack import Stack

def binary(n):
    st = Stack()

    while n > 0:
        st.push( n%2 )
        n = n //2
    res = []
    while st.length()>0:
        res.append(str(st.pop()))
    " ".join(res)
    print(res)

for i in range(300):
    binary(i)