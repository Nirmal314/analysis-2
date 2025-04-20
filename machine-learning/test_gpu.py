# import torch
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0))
# tensor = torch.tensor([1.0, 2.0]).to('cuda')
# print(tensor * 2)

import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())  # Should show 2
print(torch.cuda.get_device_name(1))  # Integrated GPU
tensor = torch.tensor([1.0, 2.0]).to('cuda:1')  # Use integrated GPU
print(tensor * 2)