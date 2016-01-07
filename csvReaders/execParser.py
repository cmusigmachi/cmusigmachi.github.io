from pprint import *

def parseFile(fname):

    ExecMem = []
    with open(fname) as f:
        for line in f:
        	x = line.split(",")
        	x.pop(0)
        	ExecMem.append(x)
    ExecMem.sort()
    pprint(ExecMem)
    for x in ExecMem:
    	if x.index(0).contains("Consul") and not x.index(0).contains("Pro"):
    		strToRet = ".box.brother.full \n" + "%" + "img.photo.left{:src => image_path('" + x.index(len(x)-1) + "')}"
    				+ "  %" + "h3 " + x.index(0) + " \n" + "  %" + "p The brothers of Sigma Chi Lambda Pi strive to be the preeminent leadership organization on our campus. We push towards this goal by stressing the importance of developing brotherhood amongst our members, as well as the importance of the strong character expected from each of our members. We work daily to create a positive impact on our members, our campus and our community. Our brotherhood is focused on fighting the negative stigma around Greek Life by behaving as leaders of good character at all times. We are always looking for emerging leaders on campus to bring into our brotherhood to support their and our own development."
    print(strToRet)

    # for name in namesNBro:
    #     strToRet = strToRet + "    %" + "li " +name
    # print(strToRet)

parseFile("execCsv.csv")

# .box.brother.full
#   %img.photo.left{:src => image_path('brothers/bill-croughan.png')}
#   %h3 Bill Croughan - President
#   %p The brothers of Sigma Chi Lambda Pi strive to be the preeminent leadership organization on our campus. We push towards this goal by stressing the importance of developing brotherhood amongst our members, as well as the importance of the strong character expected from each of our members. We work daily to create a positive impact on our members, our campus and our community. Our brotherhood is focused on fighting the negative stigma around Greek Life by behaving as leaders of good character at all times. We are always looking for emerging leaders on campus to bring into our brotherhood to support their and our own development.

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/bryce-beisswanger.png')}
#   %h3 Kevin Chiu - Vice President
#   %ul
#     %li Major: Information Systems & Economics
#     %li Year: Junior
#     %li Hometown: Brooklyn, NY
#     %li Favorite Thing: Basketball

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/kevin-chiu.png')}
#   %h3 Matthew Baker - Treasurer
#   %ul
#     %li Major: Information Systems & Economics
#     %li Year: Junior
#     %li Hometown: Brooklyn, NY
#     %li Favorite Thing: Basketball

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/gus-henry.png')}
#   %h3 Gus Henry - Annotator
#   %ul
#     %li Major: Information Systems
#     %li Year: Sophomore
#     %li Hometown: Wichita, KS
#     %li Favorite Thing: Farming

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/ryan-pearce.png')}
#   %h3 Ryan Pearce - Rush Chair
#   %ul
#     %li Major: Mechanical Engineer and BioMedical Engineer
#     %li Year: Sophomore
#     %li Hometown: Bridgewater, NJ
#     %li Favorite Thing: Soccer

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/ryan-sickles.png')}
#   %h3 Ryan Sickles - Social Chair
#   %ul
#     %li Major: Information Systems
#     %li Year: Sophomore
#     %li Hometown: Needham, MA
#     %li Favorite Thing: Meek Mill & Skiing

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/gabe-hob.png')}
#   %h3 Gabe Hobeika - Pledge Educator
#   %ul
#     %li Major: Computer Science
#     %li Year: Junior
#     %li Hometown: Alpine, NJ
#     %li Favorite Thing: Rugby

# .box.brother
#   %img.photo.left.crop{:src => image_path('brothers/zach-mansley.png')}
#   %h3 Zach Mansley - Risk Manager
#   %ul
#     %li Major: Materials Science and Engineering
#     %li Year: Junior
#     %li Hometown: Ramsey, NJ
#     %li Favorite Thing: Skiing