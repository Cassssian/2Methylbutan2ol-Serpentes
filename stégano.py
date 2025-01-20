from PIL import Image

#img = Image.open("Blaise.png")
#img2 = Image.new('RGB', (20,20))

#r,v,b = img.getpixel((0,0))
#img2.putpixel((0,0),(r,v,b))

#largeur = img.width
#hauteur = img.height

#print(r)
#img2.show()


#090968790EB
#-----------------------
# Exercice 1 : 

def msb2lsb(o, n):
    return o >> (8-n)

#print(bin(msb2lsb(0b10111011, 3)))

#-----------------------
# Exercice 2 : 

def lsb(o,n):
    return o & (2**n-1)
    #return o & int("0b" + "1" * n, 2)

    i = 0 
    mask = 0 
    while i < n : 
        mask += 2**i
        i += 1
    return o & mask 

#print(bin(lsb(0b10111011, 3)))

#-----------------------
# Exercice 3 :

def lsb2msb(o, n):
    return lsb(o,n) << (8-n) 

#print(bin(lsb2msb(0b10111011, 3)))

#-----------------------
# Exercice 4 :

def lsb2zero(o, n):
    return o & ~((1 << n)-1)
    cest_le_mask : ~((1 << n)-1)

#print(bin(lsb2zero(0b10111011, 3)) )

#-----------------------
#Décodage


def  decode_image(nom_img, n):
    image = Image.open(nom_img)
    largeur = image.width
    hauteur =  image.height
    image_decode = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))

            r_decode = lsb2msb(r, n)
            g_decode = lsb2msb(g, n)
            b_decode = lsb2msb(b, n)

            image_decode.putpixel((x, y), (r_decode, g_decode, b_decode))
    
    return image_decode.show()

decode_image("Blaise.png",1)





def fusion(img1, img2, n):

    img1 = Image.open(img1)
    img2 = Image.open(img2)

    largeur = img1.width
    hauteur =  img1.height
    
    img_fusion = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):

            r1, v1, b1 = img1.getpixel((x, y))
            r2, v2, b2 = img2.getpixel((x, y))

            r_fusion = lsb2zero(r1, n) | msb2lsb(r2, n)
            v_fusion = lsb2zero(v1, n) | msb2lsb(v2, n)
            b_fusion = lsb2zero(b1, n) | msb2lsb(b2, n)


            img_fusion.putpixel((x, y), (r_fusion, v_fusion, b_fusion))

    return img_fusion

# "noir noir noir et un blanc" - Galand 
