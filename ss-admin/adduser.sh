#! /bin/bash
useAge(){
    echo "Error Usage";
    echo "adduser [startport] [endport]"
    exit 1
}
if [ "$1" -gt 0 -a "$2" -gt 0 ] 2>/dev/null;then
    echo "check dight is ok"
else
    echo "start and end port mast is dight"
    useAge
fi
if [ "$1" -ge "$2" ];then
    echo "start port mast less than end port"
    useAge
else
    echo "begin..."
fi
for((i=$1;i<$2;i++));do
    PASSWD=$(echo "$i"|base64)
    echo $i $PASSWD
#ssadmin.sh add $i $PASSWD 200M
done
