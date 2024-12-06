for i in $(ls . | grep -v "generate");
do
    touch $i/annotations-2.txt
    printf "" > "$i/annotations-2.txt"
    for j in $(ls $i | grep -v ".txt");
    do
        printf "$j +\n" >> "$i/annotations-2.txt"
    done
done
