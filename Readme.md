# Todo
- [ ] Add floor_award to action
- [ ] Add training 1/2/4/8hr to action
- [ ] Add import function
- [ ] Update action exp

# Usage
Start your character after this line. (remind tabs)
```python
if __name__ == "__main__":
```
## Initial
Update the vals according to the character which you use. For example using kirito & 121 extra point for `luck`.
```python
if __name__ == "__main__":
    val_base   = [ 25,  3,  2,  2,  3,  6,  2,  1,  1] # 基礎值
    val_start  = [350, 38, 33, 30, 25, 20, 32, 25, 20] # 初始值
    val_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,121] # 額外值

    kirito = character(val_base, val_start, val_extra)
```
## Action
## Show
## Draw