echo '# custom DIP function
dip() {
        sh -c "docker inspect /"$1/"> $DIP_HOME/template.json" ;
        python3 $DIP_HOME/main.py ;
        rm $script_loc/template.json ;
}
export $DIP_HOME='$PWD'
export -f dip' >> ~/.bashrc;
source ~/.bashrc;
