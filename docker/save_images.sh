# Save all images in docker-compose file
#!/bin/bash

for image in $(docker-compose config | awk '{if ($1 == "image:") print $2;}'); do
  images="$images $image"
  echo "$image \n"
done
echo $images
echo "Save all images to: $1.imgs"
docker save -o $1.imgs $images