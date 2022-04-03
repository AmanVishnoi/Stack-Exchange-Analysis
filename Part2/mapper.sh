
echo -e '\n\n'
echo "The number of users per batch:"
cat Badges.xml | grep 'TagBased="False"' | awk -F'Name="|" Date' '{print $2}' 
