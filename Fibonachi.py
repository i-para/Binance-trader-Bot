import math

def fibonachi(low,high,current_price,abs_tol=0.005):
                             
        diffrent= high - low

        print("1      >>>>>>  ",high - 1 * diffrent)
        if math.isclose(high - 1 * diffrent,current_price,abs_tol=abs_tol):
            return True

        print("0.786  >>>>>>  ",high - 0.786 * diffrent)
        if math.isclose(high - 0.786 * diffrent,current_price,abs_tol=abs_tol):
            
            return True

        print("0.618  >>>>>>  ",high - 0.618 * diffrent)
        if math.isclose(high - 0.618 * diffrent,current_price,abs_tol=abs_tol):
            return True
        
        print("0.5    >>>>>>  ",high - 0.5 * diffrent)
        if math.isclose(high - 0.5 * diffrent,current_price,abs_tol=abs_tol):
            return True

        print("0.382  >>>>>>  ",high - 0.382  * diffrent)
        if math.isclose(high - 0.382 * diffrent,current_price,abs_tol=abs_tol):
            return True

        print("0.236  >>>>>>  ",high - 0.236 * diffrent)
        if math.isclose(high - 0.236 * diffrent,current_price,abs_tol=abs_tol):
            return True

        return False




fibonachi(15989,17547,16971)
































print(fibonachi(0.256500,0.64050,0.192550))

        

    

    

