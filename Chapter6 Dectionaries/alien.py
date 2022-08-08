# 字典

# 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 与大多数编程概念一样，要熟练使用字典，也需要一段时间的练习。使用字典一段
# 时间后，你就会明白为何它们能够高效地模拟现实世界中的情形。

# 使用字典  ！！！ 重点
# 在Python中，字典 是一系列键值对 。每个键 都与一个值相关联，你可使用键来访
# 问相关联的值。与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将
# 任何Python对象用作字典中的值。

# 在Python中，字典用放在花括号（{} ）中的一系列键值对表示
alien_0 = {'color': 'green', 'points': 5}

# 键值对 是两个相关联的值。指定键时，Python将返回与之相关联的值。键和值之间
# 用冒号分隔，而键值对之间用逗号分隔。在字典中，想存储多少个键值对都可以。    ！！！重点

# 最简单的字典只有一个键值对，如下述修改后的字典alien_0 所示
alien_0 = {'color': 'green'}


# 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")



# 添加键值对
# 字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典
# 名、用方括号括起的键和相关联的值。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 注意 　在Python 3.7中，字典中元素的排列顺序与定义时相同。如果将字典打
# 印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。


# 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
# 在空字典中添加键值对有时候可提供便利，而有时候必须这样做。
# 使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需
# 要先定义一个空字典。

# 修改字典中的值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'  # 有color就是改 没color就是加 都是一个句子
print(f"The alien is now {alien_0['color']}.")


# 来看一个更有趣的例子，对一个能够以不同速度移动的外星人进行位置跟踪。为
# 此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# 这个外星人的移动速度肯定很快。
 	x_increment = 3

# 新位置为旧位置加上移动距离。
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# 删除键值对

# 对于字典中不再需要的信息，可使用del 语句将相应的键值对彻底删除。使用del
# 语句时，必须指定字典名和要删除的键。  注意 　删除的键值对会永远消失。
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0

