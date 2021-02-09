#!/bin/bash
current_dir=$(cd `dirname $0` && pwd)

# P1不超过5个小时	
function p1() {
	mkp11=`mktemp`
	mkp12=`mktemp`
	lotus-sealer sealing jobs|awk '/PC1.*running\s+[0-9]+h/{sub("h",".");print $4 " " $7}' | sed 's/m.*$//' > $mkp11
	awk '$2>5{print $1}' $mkp11 | grep -Po '(\d+\.){3}\d+:\d+' | sort -n | uniq > $mkp12 
	awk -F: 'NR==1{printf"%s",$0;x=$1}NR!=1{if($1==x){printf " %s",$2}else{printf"\n%s",$0;x=$1}}END{printf "\n"}' $mkp12 > ${current_dir}/../log/p1.log
	rm -rf $mkp11 $mkp12
}


# P2不超过25min
function p2() {
	mkp21=`mktemp`
	mkp22=`mktemp`
	mkp31=`mktemp`
	mkp32=`mktemp`
	lotus-sealer sealing jobs|awk '/PC2.*running\s+[0-9]+m/{print $4 " " $7}' | sed 's/m.*$//' > $mkp21
	awk '$2>25{print $1}' $mkp21 | grep -Po '(\d+\.){3}\d+:\d+' | sort -n | uniq > $mkp22 
	# awk -F: 'NR==1{printf"%s",$0;x=$1}NR!=1{if($1==x){printf " %s",$2}else{printf"\n%s",$0;x=$1}}END{printf "\n"}' $mkp22
	awk -F: 'NR==1{printf"%s",$0;x=$1}NR!=1{if($1==x){printf " %s",$2}else{printf"\n%s",$0;x=$1}}END{printf "\n"}' $mkp22 > ${current_dir}/../log/p2.log
	lotus-sealer sealing jobs|awk '/PC2.*running\s+[0-9]+h/{sub("h",".");print $4 " " $7}' | sed 's/m.*$//' > $mkp31
	awk '$2>1{print $1}' $mkp31 | grep -Po '(\d+\.){3}\d+:\d+' | sort -n | uniq > $mkp32
	# awk -F: 'NR==1{printf"%s",$0;x=$1}NR!=1{if($1==x){printf " %s",$2}else{printf"\n%s",$0;x=$1}}END{printf "\n"}' $mkp32
	awk -F: 'NR==1{printf"%s",$0;x=$1}NR!=1{if($1==x){printf " %s",$2}else{printf"\n%s",$0;x=$1}}END{printf "\n"}' $mkp32 >> ${current_dir}/../log/p2.log
	rm -rf $mkp21 $mkp22 $mkp31 $mkp32
}


# C2不超过1个小时
function c2() {
	mkpc1=`mktemp`
	mkpc2=`mktemp`
	lotus-sealer sealing jobs|awk '/\<C2\>.*running\s+[0-9]+h/{sub("h",".");print $4 " " $7}' | sed 's/m.*$//' > $mkpc1
	awk '$2>1{print $1}' $mkpc1 | grep -Po '(\d+\.){3}\d+:\d+' | sort -n | uniq > $mkpc2
	awk -F: 'NR==1{printf"%s",$0;x=$1}NR!=1{if($1==x){printf " %s",$2}else{printf"\n%s",$0;x=$1}}END{printf "\n"}' $mkpc2 > ${current_dir}/../log/c2.log
	rm $mkpc1 $mkpc2
}

function main() {
	source /etc/profile
	case $1 in
	 p1)
		  p1
	          if [ $? == 0 ] ; then
	                  echo p1 success;
	          else 
			  echo p1 failed;
	          fi
	 ;;
	 p2)
	          p2
	          if [ $? == 0 ] ; then
	                  echo p2 success;
	          else 
			  echo p2 faied;
	          fi
	 ;;
	 c2)
	          c2
	          if [ $? == 0 ]; then
	                  echo c2 success;
	          else 
			  echo c2 failed;
	          fi
	;;
	*)
		echo "Usage:
		      	bash timeout.sh p1|p2|c2
		"
	esac	
}

main ${1}
