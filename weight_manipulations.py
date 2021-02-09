from new_funcs import *
from functions import *

path = 'C:/Users/crowl/github/jsr_pigs/Weight_Data.csv'
weight_data = get_data_frame(path)

weaning_dates = weight_data['Date']  # Date weaned
weight_after_weaning = weight_data['Average Weight']  # A weight that corresponds to a certain number of days after weaning
days_post_wean = weight_data['Days Post Wean']  # The certain number of days that the above weight corresponds to
weight_out = weight_data['Weight Out']  # The weight that they leave the farm for the slaughter house
days_in = weight_data['Days in']  # At this date after weaning, they will have been in the building for 1 days. This is the number of days in the building
fat_depth = weight_data['P2']  # The fat depth at which they are sold

plt.scatter(weight_out, fat_depth)
plt.xlabel('Weight when sold')
plt.ylabel('Fat depth when sold')
plt.show()