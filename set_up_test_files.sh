set -e

files=("test1.txt" "test2.pdf" "test3.csv" "test4.exe" "test5.mp3" "test6.mp4" "test7.png" "test8.rar" 'test with spaces and sp $ !.pdf' "test with spaces .txt" "no ext test")
folders=("test" "test/archive" "test/data" "test/documents" "test/exe" "test/video" "test/image" "test/music" "test/src")

for f in ${folders[@]}; do
    mkdir $f
done

for f in "${files[@]}"; do
    echo "creating file: $f"
    touch "test/src/$f"
done
