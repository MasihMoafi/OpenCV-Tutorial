"""
🔥 TENSOR MASTERY: NumPy & PyTorch
From Zero to Karpathy-Level Matrix Ninja

Run each section to learn tensor operations for transformers
"""

import numpy as np
import torch

print("="*60)
print("PART 1: TENSOR FUNDAMENTALS")
print("="*60)

# Scalar (0D)
scalar = torch.tensor(5)
print(f"Scalar: {scalar}, shape: {scalar.shape}")

# Vector (1D)
vector = torch.tensor([1, 2, 3])
print(f"Vector: {vector}, shape: {vector.shape}")

# Matrix (2D)
matrix = torch.tensor([[1, 2], [3, 4]])
print(f"Matrix:\n{matrix}\nshape: {matrix.shape}")

# 3D Tensor
tensor_3d = torch.randn(2, 3, 4)  # (batch, seq, features)
print(f"3D Tensor shape: {tensor_3d.shape}")

print("\n" + "="*60)
print("PART 2: INDEXING & SLICING")
print("="*60)

x = torch.randn(4, 5, 6)  # (batch, seq, features)
print(f"Original shape: {x.shape}")
print(f"First batch: {x[0].shape}")
print(f"First 2 batches: {x[:2].shape}")
print(f"First 3 tokens: {x[:, :3].shape}")
print(f"Last feature: {x[:, :, -1].shape}")

# Boolean masking
mask = x > 0
print(f"Positive values count: {x[mask].shape[0]}")

print("\n" + "="*60)
print("PART 3: BROADCASTING (THE SECRET SAUCE)")
print("="*60)

# Add scalar to matrix
x = torch.randn(3, 4)
y = 5
z = x + y
print(f"Matrix + scalar: {x.shape} + scalar = {z.shape}")

# Add vector to matrix
x = torch.randn(3, 4)
y = torch.randn(4)
z = x + y
print(f"Matrix + vector: {x.shape} + {y.shape} = {z.shape}")

# Add column vector
x = torch.randn(3, 4)
y = torch.randn(3, 1)
z = x + y
print(f"Matrix + column: {x.shape} + {y.shape} = {z.shape}")

# Unsqueeze for broadcasting
x = torch.randn(3, 4)
y = torch.randn(3)
y = y.unsqueeze(1)  # Make it (3, 1)
z = x + y
print(f"With unsqueeze: {x.shape} + {y.shape} = {z.shape}")

print("\n" + "="*60)
print("PART 4: MATRIX OPERATIONS")
print("="*60)

# Matrix multiplication
A = torch.randn(3, 4)
B = torch.randn(4, 5)
C = A @ B
print(f"Matmul: {A.shape} @ {B.shape} = {C.shape}")

# Batch matmul
A = torch.randn(32, 3, 4)
B = torch.randn(32, 4, 5)
C = A @ B
print(f"Batch matmul: {A.shape} @ {B.shape} = {C.shape}")

# Broadcasting in matmul
A = torch.randn(32, 3, 4)
B = torch.randn(4, 5)
C = A @ B
print(f"Broadcast matmul: {A.shape} @ {B.shape} = {C.shape}")

# Einsum (attention mechanism)
Q = torch.randn(32, 8, 10, 64)  # (batch, heads, seq, d_k)
K = torch.randn(32, 8, 10, 64)
scores = torch.einsum('bhqd,bhkd->bhqk', Q, K)
print(f"Einsum attention: Q{Q.shape} @ K^T = {scores.shape}")

print("\n" + "="*60)
print("PART 5: RESHAPING & TRANSPOSING")
print("="*60)

x = torch.randn(32, 10, 512)
print(f"Original: {x.shape}")

# Flatten
x_flat = x.reshape(-1)
print(f"Flattened: {x_flat.shape}")

# Reshape to 2D
x_2d = x.reshape(32, -1)
print(f"2D: {x_2d.shape}")

# Split into heads
x_heads = x.reshape(32, 10, 8, 64)
print(f"Split heads: {x_heads.shape}")

# Transpose
x_t = x.transpose(-1, -2)
print(f"Transposed: {x_t.shape}")

# Permute
x = torch.randn(32, 8, 10, 64)
x_perm = x.permute(0, 2, 1, 3)
print(f"Permuted: {x.shape} -> {x_perm.shape}")

print("\n" + "="*60)
print("PART 6: ADVANCED TRICKS")
print("="*60)

# Masked fill (causal mask)
x = torch.randn(4, 4)
mask = torch.triu(torch.ones(4, 4), diagonal=1).bool()
x_masked = x.masked_fill(mask, float('-inf'))
print(f"Causal mask applied: {x_masked.shape}")
print(f"Mask:\n{mask.int()}")

# Concatenation
x = torch.randn(3, 4)
y = torch.randn(3, 2)
z = torch.cat([x, y], dim=1)
print(f"Concat: {x.shape} + {y.shape} = {z.shape}")

# Stack
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.stack([x, y], dim=0)
print(f"Stack: {x.shape} + {y.shape} = {z.shape}")

print("\n" + "="*60)
print("PART 7: TRANSFORMER OPERATIONS")
print("="*60)

# Multi-head attention reshaping
batch_size, seq_len, d_model = 32, 10, 512
n_heads, d_k = 8, 64

x = torch.randn(batch_size, seq_len, d_model)
print(f"Input: {x.shape}")

# Split into heads
Q = x.reshape(batch_size, seq_len, n_heads, d_k)
print(f"After reshape: {Q.shape}")

Q = Q.transpose(1, 2)
print(f"After transpose: {Q.shape} (batch, heads, seq, d_k)")

# Attention scores
K = Q
scores = Q @ K.transpose(-1, -2)
print(f"Attention scores: {scores.shape}")

# Scale
scores = scores / (d_k ** 0.5)

# Softmax
attn = torch.softmax(scores, dim=-1)
print(f"Attention weights: {attn.shape}")

# Apply attention
V = Q
out = attn @ V
print(f"Attention output: {out.shape}")

# Concatenate heads
out = out.transpose(1, 2).reshape(batch_size, seq_len, d_model)
print(f"Final output: {out.shape}")

print("\n" + "="*60)
print("🏆 KARPATHY'S PRO TIPS")
print("="*60)
print("""
1. Always print shapes during debugging
2. Use assertions to catch shape errors early
3. Prefer @ over torch.matmul for readability
4. Use einsum for complex operations
5. Remember: view requires contiguous, reshape doesn't
6. Broadcasting is your friend - master it!
7. Use .unsqueeze() and [:, None] liberally
8. Transpose last 2 dims with .transpose(-1, -2)
9. Always .contiguous() after transpose/permute
10. Test with small tensors first, then scale up
""")

print("\n" + "="*60)
print("✅ TENSOR MASTERY COMPLETE!")
print("="*60)
print("Now go build transformers! 🚀")
