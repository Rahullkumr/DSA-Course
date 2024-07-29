# Input a complex number and display the greater number between real and imaginary part

print("Complex number: X + Yj  Eg: 2 + 3j \n")

complex_no = complex(input("Enter a complex number in (X+Yj) format: "))

print("Greater part is: ", end=" ")
print(f"Real part {complex_no.real}" if complex_no.real > complex_no.imag else f"Imaginary part {complex_no.imag}")