import json
import random

""""
Banner taken from https://www.asciiart.eu/books/lord-of-the-rings
Credited to Blazej Kozlowski
"""
banner = """             ___ . .  _                                                                                             
    "T$$$P"   |  |_| |_                                                                                             
     :$$$     |  | | |_                                                                                             
     :$$$                                                      "T$$$$$$$b.                                          
     :$$$     .g$$$$$p.   T$$$$b.    T$$$$$bp.                   BUG    "Tb      T$b      T$P   .g$P^^T$$  ,gP^^T$$ 
      $$$    d^"     "^b   $$  "Tb    $$    "Tb    .s^s. :sssp   $$$     :$; T$$P $^b.     $   dP"     `T :$P    `T
      :$$   dP         Tb  $$   :$;   $$      Tb  d'   `b $      $$$     :$;  $$  $ `Tp    $  d$           Tbp.   
      :$$  :$;         :$; $$   :$;   $$      :$; T.   .P $^^    $$$    .dP   $$  $   ^b.  $ :$;            "T$$p.  
      $$$  :$;         :$; $$...dP    $$      :$;  `^s^' .$.     $$$...dP"    $$  $    `Tp $ :$;     "T$$      "T$b 
      $$$   Tb.       ,dP  $$\"""Tb    $$      dP ""$""$" "$"$^^  $$$""T$b     $$  $      ^b$  T$       T$ ;      $$;
      $$$    Tp._   _,gP   $$   `Tb.  $$    ,dP    $  $...$ $..  $$$   T$b    :$  $       `$   Tb.     :$ T.    ,dP
      $$$;    "^$$$$$^"   d$$     `T.d$$$$$P^"     $  $\"""$ $"", $$$    T$b  d$$bd$b      d$b   "^TbsssP" 'T$bgd$P
      $$$b.____.dP                                 $ .$. .$.$ss,d$$$b.   T$b.
    .d$$$$$$$$$$P  bug
"""
with open('quotes.json') as f:
    data = json.load(f)
    quote_dict = random.choice(data)
    print(banner)
    print(f""""{quote_dict['quote']}"\n""")
    source = quote_dict['source']
    if source != "":
        print(f"- {source}")
    print(quote_dict['book'])