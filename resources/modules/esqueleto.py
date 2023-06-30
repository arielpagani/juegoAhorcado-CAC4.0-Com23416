def figura(errores):
    match errores:
        case 0:
            return print("""
                    +-----+
                    |
                    |		
                    |		
                    |		
                   ===
                  ===== 
                  """)
        case 1:
            return print("""
                    +-----+
                    |	  O	
                    |		
                    |
                    |		
                   ===
                  ===== 
                  """)
        case 2:
            return print("""
                    +-----+
                    |     O		
                    |     |	
                    |
                    |		
                   ===
                  ===== 
                  """)
        case 3:
            return print("""
                    +-----+
                    |	  O	
                    |    /|	
                    |
                    |		
                   ===
                  ===== 
                  """)
        case 4:
            return print("""
                    +-----+
                    |	  O	
                    |    /|\	
                    |
                    |		
                   ===
                  =====
                  """)
        case 5:
            return print("""
                    +-----+
                    |     O	
                    |    /|\	
                    |    /	
                    |
                   ===
                  ===== 
                  """)
        case 6:
            return print("""
                    +-----+
                    |     O	
                    |    /|\  GAME		
                    |    / \	OVER
                    |
                   ===
                  =====    
            
                  """)
