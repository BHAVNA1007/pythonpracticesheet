from  .total_marks import cal_marks


def percentage(marks):
   
    total = cal_marks(marks)
  
    return (total/500)*100