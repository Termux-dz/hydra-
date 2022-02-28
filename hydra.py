import os,time
os.system('pkg install get')
os.system('clear')
print('\033[1;33mwelcome ye my tools') 
logo = """\033[1;32m
                                                   ~ ف! .؟ PB ^                                
                                                  YGB. ~ PGB7                                 
                                                 YG5G ^ ~~! 7؟ JJYG5GY                                  
                                                7B55PPPPP5555555GG ^.                          
                                               ؟ 55YYYYY5YYY5Y؟ PP5PB: .Y77 ~~~~~~ ^^ ~! ^              
                                              .B75555555YY5YJ5P؟ ~ YBY 7؟ . ::: ^^ ~~! ^ YY              
                                          :::! 5G5555YYYYYY55557 ~: YPB. ^ 5: ~~ ^^: ...... ~ GY:            
                                         ؟ Y77JYP5555555555P5J7 ~ ^! G ~ 5P # ~: GJ ~ YGGGY ^! 7 ~:. ~ GG!           
                                         . ^ 7Y.: YPPPPPP5Y7 ^ ..:! 5G755B! ~؟ P ^ ^ B5JY5GG5Y ^: ~ J # ؟.         
                       .! PJ ^؟ ~: ^ ~~~~ ^ :. J؟ .. ^ ~~~~ ^ ..!؟ PG!؟ P5BPJ. ^ 7؟ 55YJ ~ 7GPPPPGJ! GBGJ:       
                     ^؟ PGGGGBGPGGGGBB # P ~:! J ~ ^ J7777؟ Y!: 7PGP ^: 5P5 ##.: ^ ^ :: ^ ~. :: ^: 5BBG ^؟ GGGG!      
                 ^ 7J5PP555555PPPPPPPPGBBBPY7..7 ~ JG5 ## GPPPPGGGP ^ 7P5PB5 ^ Y !! 757 ^ ~~! ~. ~ 7! 7 ^! BB # G # J     
              ~؟ 5PP55YY55YYYJJJY5PPP55PPGB # & YYG! ~ GGP77Y؟ GBG؟ !! YP5GBGPY؟ J :::: ^ ~: ~ ^ :: ~ PBB # 75 & J    
           :؟ PPGPYY؟: ^ !! ^^ ~. .. ^ ~~ 7YPP55PG # GJYY! Y5Y! ~! JY.7P!:!؟ PPGB &&&؟ .P ^ :: ^ ^ ^ ~ 7 ^ ::: 7BGB # ^ ^^    
         ~ YGP775J؟! ~~: ~ .. ^ ..: ^^:. :::! YPP5PGBP: ؟؟: .. .....: ~ 7P5B & P: ~ ^؟ Y .... ^ 77 ~: ::. JBGB # ~       
      :! YG5؟ ~! J77PGG! ~~ 7؟ 7777777! ^ ... ^ YP55PB # B ^ YJ! ~ ^^ ~~~: ^ ~ 7P5GP ^: .J7: .. ::: ~ ^ ::: 7GGGB # ^       
     757 ^: ..! G! ~ PJ؟ : جي !. . ~ Y؟ ::. 7PP5PB # GB ~ 5 ~!: ...: ^؟ ~ 7PPB # ~ ~ J7 ..... :::::: 7GGGGBB.       
      ^! 7! ~! G & ~ PY ~: ~ J7 .P!:. 7PP5PB # ؟! 5Y7 ~ :: ~ !!! ~ 7PPB؟ ~ ^ Y7. . :::::::::: ^ JGGGGPBY        
         . :: ^ ~ 5؟ G؟ ^ ؟؟:؟ 5 :: JP5PB # & GY ~ 7! ^ .. ^ 77 ~؟ PB # Y.! 777 ^. :: .... ^^ 5GGGGPB:        
              ~ 5 ^^ Y ~ 5!:! 5P5G && G ~ ::: ^ ::::: ~ JPGBY ~~ 7J!:. ..: ^^ :::: ^ 75GGGGG # BB؟         
               ! 55 ^ J7: ^ YPPP557 ~ ^ ^ ^ :: ...: 75PG # P؟ 7 ~: ..: ^^: .. ::: ^^ ~؟ 5PPPGPPBG & J          
               ؟ & 5: 7 ~: ^ JPP5J ~ ::::::: ..: ^! YPY؟ 77! ^ :: ....: ^^ ~ ^ :: ~ 7YPPPGB # BPBJ :؟           
               ~ G # B5. !؟ ^ ^ ^ JPY! ^^ .: ^ ^ ^ ^ :::: ~ 7؟ YPGPGGB # PBBG!              
                ~ ب # ص. .J! :: ^ Y57 :::::::::.: ^^ 77 ~ ^: ..: ^ ::::::: ~~!؟ YPPGB # BPPBP7.5Y:               
                 ..: 5! ^^: JY ~ ^^uable ^ ^ ^ ^:.: ^ ^ ^ ^ ^ ^ ^ ^: ...: ^ ^ ^ ^ ~!                     
                          : P!: ^^ 7؟ ^ :::: ^^ ^^ ^^ authاوي ^ ::::: ^^ ^^ ~ ^: ^ ~!؟ Y5PGGPG5GGJ ؟؟ PG # P7.                    
                          5؟ ::: ^؟                
                         ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^؟             
                         ! 5 :::: ~~ ::::: ~ ^ :: ^ ^ ^ ^ ::: ^ ^ ^ ~ YPPPPPPPPPPPP5PPPPPPPPPPPPPPPPGGBBP          
                         ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^: ^ ::: ^ ^ ^ ^ ^ ^ ^ ^ :::؟        
                          P7: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ YPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGBBJ       
                          ^ G ~: ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^      
                           ~ P ~: ^ ^ ^ ^ ^ ^ ^ ^ ^: ^^     
                            ^ P؟ :::::::::::::: ^ ^^     
                             .Y5 ~ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ::: ^!     
                               ! YJ ~: ^ ^ ^ ^ ^ ^ ^ ^ ^ :::::::: ^ ^^: ^ ^: ^ !؟ Y55PPPPPGGPJ ~ :. JBGGBBB ^      
                                 ~ JJ7 ~ ^ :::::: ^ ^ ^ ^ ^ ~ ^ ^ ^ ^ ^:. . ::: ~ 7JPPY7 ^ 5BGB # P:       
                                   . ~ 77 ؟؟ ~ ^^ ~ ^ ^ ^ ^ ^ :::::: ^^ ~ 77777 !! ^ :. ..... ~؟ PBBBG7         
                                    ^ J75BGPG557؟ 5Y ؟؟ YJYPJ؟! ~ ^ ... ^! JY5PPGGPP55YJJY5GGBBB5 !.          
                                   : BBGGG #؟ 5GB.؟ BBBGPGB7 ^ JPGBGP55YY555PGBBBGGGB57:             
                                   .5 & BG! YY ^! .5 # & #؟ # P .YGGGJ ~ :. ..: ^ !؟ YGP                
                                    . ^. !! ^ 7 ب ~ !. 5GGP:: 7Y5B؟                
                                                   . ~ # PB:.! YGP5YB ^                
                                                          ^ # PG ~؟ G # BBBPP                 
                                                           ؟ BPGP؟ ^. :! YGGP! ~ B7                 
                                                            ^ J5GGGG5YJY5PBBGY ~.                  
                                                               :!؟ YPPGP5Y؟ ~.                        
       ╔═✦•ೋ°♤♤°ೋ•✦═╗
   \033[1;31mtermux dz hydra install
​​       ╚═✦•ೋ°♤♤°ೋ•✦═╝"""
print(logo)
time.sleep(4)
os.system('get clone https://github.com/vanhauser-thc/thc-hydra ')
os.system('cd thc-hydra')
os.system('./configure ')
os.system('make install')
os.system('clear')
print('\033[1;31mThe installation was very thankful termux dz') 
os.system('./hydra -help') 