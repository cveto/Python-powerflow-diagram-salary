#  Libraries
import turtle
import math

upmore=0    # Keeping arrows at the same height

# Start the turtle. Name it Bob.
bob = turtle.Turtle()
bob.penup()
bob.left(180)
bob.forward(300)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.pendown()

def arrow_eating(width,height,orientation,eating):
    print("Hello from a function")
    x=width   # Širina puščica - cena stroška
    d=height  # Višina puščice - samo lepotno
    fid=60    # Kot puščice
    r=0       # polmer malega zavoja
    
    fir=math.radians(fid)    # fid v radianih
    fi_arrowpoint=180-fid    # Kot vrha puščice - da se ujame nazaj na vodoravno
    R=r+x                    # Polmer velikega zavoja. odvisen od X zato da se ujame s sirino
    z=x/6                    # nadstreha puščice
    llevo=z                  # Črta preden se puscica zacne
    ldesno=x+2*z             # Črta ko se puscica konca
    y=(x/2+z)/math.cos(fir)  # Dolzina posevnice pri puscici
    

    ## Orientation
    bob.right(orientation)
    
    if eating == "yes":
        bob.forward(llevo)
        bob.circle(r,90)
    else:
        bob.left(90)
    
    bob.forward(d)
    bob.forward(upmore)               # Ujemanje visine s prejsnjo pusico, rabi vhod prejsnje
    
    bob.left(90)
    bob.forward(z)
    
    bob.right(180)
    bob.left(fid)  # Arrow sideways
    bob.forward(y)
    
    bob.right(fi_arrowpoint)
    bob.forward(y)
    
    bob.right(60+fid)
    bob.forward(z)
    
    bob.left(90)
    bob.forward(d)

    
    if eating == "yes":
        bob.forward(upmore)
        bob.right(180)
        bob.circle(R,-90)
        bob.forward(ldesno)

    else:
        bob.left(90)
        bob.forward(2*z)
        
 
    
    return x

#upmore=arrow_up2(debelina puscice,visina_puscice,orientacija)
bob.forward(20)
arrow_eating(74.439,60,0,"yes")
arrow_eating(44.29,60,0,"yes")
arrow_eating(3.629,60,0,"yes")
arrow_eating(3.178,60,0,"yes")
arrow_eating(2.186,60,0,"yes")
arrow_eating(209.9,60,90,"no")
arrow_eating(12.9,60,0,"no")
arrow_eating(12.9,60,0,"no")







print(math.cos(math.pi/6))

# Step 4: We're done!
turtle.done()
