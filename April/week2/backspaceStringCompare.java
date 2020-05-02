 public boolean backspaceCompare(String S, String T) {
        int n = S.length();
        int m = T.length();
        char[] schar = S.toCharArray();
        char[] tchar = T.toCharArray();
        for(int i = 1;i<n;i++){
            if((schar[i] == '#') && (schar[i-1] != '#')){
                schar[i-1] = '#';
            }  
        }

        for(int j = 1; j<m; j++){
            if((tchar[j] == '#') && (tchar[j-1] != '#')){
                tchar[j-1] = '#';
            }
        }
        s_string = new String(schar);
        t_string = new String(tchar);

        System.out.println(t_string);
        System.out.println(s_string);
        return true;
    }


