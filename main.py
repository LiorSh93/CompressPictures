from PIL import Image, ImageOps
import glob

#Compress Script
location_Original_Pictures = "YOURPATH\\*.%s"
location_Compressed_Pictures = "YOURDESTPATH\\"
legal_picture_types = ["jpg", "png"]

#Make list of all pictures full paths
image_list = [item for i in [glob.glob(location_Original_Pictures % ext) for ext in legal_picture_types] for item in i]
#The loop will go over all your images in the folder, compress and save in new location
for image_location in image_list:
    picture = Image.open(image_location)
    #fix image orientation due to tagging problem in camera phones
    fixed_picture = ImageOps.exif_transpose(picture)
    #Get The file name
    image_location_file_names_list = image_location.split("\\")
    image_file_name = "Comp" + image_location_file_names_list[len(image_location_file_names_list) - 1]
    # compress and save in new location
    new_save_location = location_Compressed_Pictures + image_file_name
    fixed_picture.save(new_save_location, optimize=True, quality=40, format="JPEG")
    print("Saved ", image_file_name, "At : ", location_Compressed_Pictures)

print("Finished, you can go check your files.")
