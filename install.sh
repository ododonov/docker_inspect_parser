echo '# custom DIP function
dip() {
        export DIP_RESULT=$(docker inspect /"$1/")
        python3 $DIP_HOME/main.py ;
}
export $DIP_HOME='$PWD'
export -f dip' >> ~/.bashrc && source ~/.bashrc
