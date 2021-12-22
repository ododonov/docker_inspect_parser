echo '# custom DIP function
dip() {
        local script_loc='$PWD' ;
        sh -c "docker inspect /"$1/"> $script_loc/template.json" ;
        python3 $script_loc/main.py ;
        rm $script_loc/template.json ;
}

export -f dip' >> ~/.bashrc;
source ~/.bashrc;
