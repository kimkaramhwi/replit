def get_prefix(strs): 
  if len(strs) == 0: 
    return ""

  prefix = "" 
  strs = sorted(strs) 
  
  for i in strs[0]: 
    if strs[-1].startswith(prefix+i): 
      result += i 
    else: 
      break 
    
  return result

