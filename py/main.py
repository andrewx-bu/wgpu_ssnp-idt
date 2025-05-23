import numpy as np
import torch
import ssnp_model

def test_scatter_factor():
    n = np.array([5, 21, 65])
    python_result = ssnp_model.scatter_factor(n)

    print("Python scatter_factor result:")
    print(python_result)

def test_c_gamma():
    res = (0.1, 0.4, 0.1)
    shape = (3, 3)
    gamma_result = ssnp_model.c_gamma(res, shape)

    print("Python c_gamma result:")
    print(gamma_result)

def test_diffract():
    uf = np.array([[1.0 + 9.0j, 2.0 + 8.0j, 3.0 + 7.0j], 
                   [4.0 + 6.0j, 5.0 + 5.0j, 6.0 + 4.0j], 
                   [7.0 + 3.0j, 8.0 + 2.0j, 9.0 + 1.0j]])
    ub = np.array([[9.0 + 1.0j, 8.0 + 2.0j, 7.0 + 3.0j], 
                   [6.0 + 4.0j, 5.0 + 5.0j, 4.0 + 6.0j], 
                   [3.0 + 7.0j, 2.0 + 8.0j, 1.0 + 9.0j]])
    res = (.1, .1, .1)
    dz = 1
    uf_new, ub_new = ssnp_model.diffract(uf, ub, res, dz)

    print("Python diffract result (uf_new):")
    print(uf_new)
    print("Python diffract result (ub_new):")
    print(ub_new)

def test_binary_pupil():
    shape = (3, 3)
    na = 0.9
    res = (0.1, 0.4, 0.1)
    mask = ssnp_model.binary_pupil(shape, na, res)

    print("Python binary_pupil result:")
    print(mask)

def test_tilt():
    shape = (2, 2)
    angles = torch.tensor([2 * torch.pi, torch.pi / 2, torch.pi /6]) 
    NA = 0.5
    res = (0.69, 0.2, 0.1)
    trunc = False
    tilt_result = ssnp_model.tilt(shape, angles, NA, res, trunc)

    print("Python tilt result:")
    print(tilt_result)

def test_merge_prop():
    res = (0.1, 0.1, 0.1)
    uf = torch.tensor([[1.0 + 9.0j, 2.0 + 8.0j, 3.0 + 7.0j], 
                       [4.0 + 6.0j, 5.0 + 5.0j, 6.0 + 4.0j], 
                       [7.0 + 3.0j, 8.0 + 2.0j, 9.0 + 1.0j]], dtype=torch.complex64)
    ub = torch.tensor([[9.0 + 1.0j, 8.0 + 2.0j, 7.0 + 3.0j], 
                       [6.0 + 4.0j, 5.0 + 5.0j, 4.0 + 6.0j], 
                       [3.0 + 7.0j, 2.0 + 8.0j, 1.0 + 9.0j]], dtype=torch.complex64)
    
    uf_new, ub_new = ssnp_model.merge_prop(uf, ub, res)
    
    print("Python merge result (uf_new):")
    print(uf_new)
    print("Python merge result (ub_new):")
    print(ub_new)

def test_split_prop():
    res = (0.1, 0.1, 0.1)
    uf = torch.tensor([[1.0 + 9.0j, 2.0 + 8.0j, 3.0 + 7.0j], 
                       [4.0 + 6.0j, 5.0 + 5.0j, 6.0 + 4.0j], 
                       [7.0 + 3.0j, 8.0 + 2.0j, 9.0 + 1.0j]], dtype=torch.complex64)
    ub = torch.tensor([[9.0 + 1.0j, 8.0 + 2.0j, 7.0 + 3.0j], 
                       [6.0 + 4.0j, 5.0 + 5.0j, 4.0 + 6.0j], 
                       [3.0 + 7.0j, 2.0 + 8.0j, 1.0 + 9.0j]], dtype=torch.complex64)
    
    uf_new, ub_new = ssnp_model.split_prop(uf, ub, res)
    
    print("Python split result (uf_new):")
    print(uf_new)
    print("Python split result (ub_new):")
    print(ub_new)

if __name__ == "__main__":
    #test_scatter_factor()
    #test_c_gamma()
    #test_diffract()
    #test_binary_pupil()
    test_tilt()
    #test_merge_prop()
    #test_split_prop()
