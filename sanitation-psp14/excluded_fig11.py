  def syn_Method_replace(self, ctx, node):                                      
    [rx, exp] = node.args                                                       
    if not isinstance(rx, ast.Str):                                             
      raise atlang.TypeError("...", node)                                       
    rx = rx.s                                                                   
    exp_t = ctx.syn(exp)                                                        
    if not isinstance(exp_t, stringin):                                         
      raise atlang.TypeError("...", node)                                       
    exp_rx = exp_t.idx                                                          
    return stringin[lreplace(self.idx, rx, exp_rx)]                             
                                                                                
  def trans_Method_replace(self, ctx, node):                                    
    return astx.quote(                                                          
      """__import__(re); re.sub(%0, %1, %2)""",                                 
      astx.Str(s=node.args[0]),                                                 
      astx.copy(node.func.value),                                               
      astx.copy(node.args[1]))                                                  




also this text:
The regular expressions describing the first character and remaining characters of a matching string in the language $\lang{r}$ must be determined to correctly specify the static semantics. For instance, the first character of a string in the language $\lang{(A\cdot B\cdot C)+(D\cdot E\cdot F)}$ is in the language $\lang{A+D}$ and the remaining characters are in the language $\lang{(B\cdot C)+(E \cdot F)}$. 
