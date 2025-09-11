# 🛠️ Useful Python Utilities

This repository contains a collection of utility modules that I frequently use across various research and development projects.  
Each module is designed for convenience, batch processing, and compatibility with commonly used libraries such as `scipy`, `PyTorch`, and `3D Slicer`.

---

## `common.py`

This module provides simple and commonly needed utilities, such as:

- `listdir()`: Returns a list of directory contents sorted in natural order.
- `make_dir()`: Creates a directory with all permissions open (read/write/execute for all users).

These functions are useful for file management in scripting environments.

---

## `transforms.py`

This module implements various representations and conversions for **rigid body transformation**:

- Supports both **6D vector** and **4×4 matrix** representations
- Allows flexible backend selection (`scipy`, `pytorch3d`, etc.)
- Built with **batch processing** in mind

Convenient methods such as `rel_to_abs`, `abs_to_rel`, and matrix composition are provided based on efficient tensor operations.

---

## `utils_slicer.py`

This module contains automation scripts designed to run inside the **3D Slicer** Python environment.  
Functions include:

- Automatic loading of volumetric data
- 3D rendering setup
- Screenshot capturing and saving

These tools are helpful for reproducible visualization and figure generation from medical imaging data.  
**⚠️ Note**: This tool is designed for a very task-specific purpose.
Please use this code only as a reference to understand how **3D Slicer** can be utilized with **Python**.

---

## 📌 Notes
- All modules are self-contained and designed to minimize dependencies.
- Most functions support both single-instance and batched inputs.
- Feel free to integrate these into your own research pipelines.