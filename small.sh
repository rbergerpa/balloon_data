for f in *.png ; do
    sips -Z 500 $f --out small/$f
done
