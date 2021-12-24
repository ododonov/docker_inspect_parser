echo '# custom DIP function
dip() {
        declare $DIP_RESULT=$(docker inspect /"$1/")
        python3 $DIP_HOME/main.py ;
        rm $DIP_HOME/template.json ;
}
export $DIP_HOME='$PWD'
export -f dip' >> ~/.bashrc && source ~/.bashrc
