class Login:
    def loginUser(self):
        print("<<Login dear User")
class OTPlogin(Login):
    def loginUser(self,phone):
        print("<<OTP login Done!!!")

class GoogleLogin(Login):
    def loginUser(self,email,password):
        print("<<Google login done")
class FBlogin(Login):
    def loginUser(self,FBID,password):

        print("<<FB login Done!!!")


class cab:
    def bookCab(self,source,destination):
        print("Cab booked from {} to {}".format(source,destination))

class OLAmicro(cab):
    def bookCab(self, source, destination):
        print(" OLA micro Cab booked from {} to {}".format(source, destination))
class OLAmini(cab):
    def bookCab(self, source, destination):
        print("OLA mini Cab booked from {} to {}".format(source, destination))
class OLAsedan(cab):
    def bookCab(self, source, destination):
        print("Cab booked from {} to {}".format(source, destination))

l=Login()
l.loginUser()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
GL=GoogleLogin()
GL.loginUser("john@ex.com","pass12334")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
FB=FBlogin()
FB.loginUser("john@ex.com","pass123")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
PH=OTPlogin()
PH.loginUser("98876643256")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

c=cab()
c.bookCab("Silver arc","MBD")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
o=OLAmicro()
o.bookCab("Silver arc","MBD")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
M=OLAmini()
M.bookCab("Silver arc","MBD")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
S=OLAsedan()
S.bookCab("Silver arc","MBD")







