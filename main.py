from hexint import number_of_bytes, hex_to_little_endian, hex_to_big_endian, little_endian_to_hex, big_endian_to_hex
#Task 1-2: hex to litlle endian, hex to big endian
# Vector 1
print('Task 1-2: hex to litlle endian, hex to big endian')
print('\nVector 1')
value='ff00000000000000000000000000000000000000000000000000000000000000'
print('Value:', value)
number_of_bytes(value)
hex_to_little_endian(value)
hex_to_big_endian(value)
# Vector 2
print('\nVector 2')
value='aaaa000000000000000000000000000000000000000000000000000000000000'
print('Value:', value)
number_of_bytes(value)
hex_to_little_endian(value)
hex_to_big_endian(value)
# Vector 3
print('\nVector 3')
value='FFFFFFFF'
print('Value:', value)
number_of_bytes(value)
hex_to_little_endian(value)
hex_to_big_endian(value)
# Vector 4
print('\nVector 4')
value='F000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
print('Value:', value)
number_of_bytes(value)
hex_to_little_endian(value)
hex_to_big_endian(value)
#Task 3: little endian to hex
print('\nTask 3: little endian to hex')
# Vector 1
print('\nVector 1')
little_endian=255
little_endian_to_hex(little_endian)
number_of_bytes(value)
print('Little endian:', little_endian)
# Vector 2
print('\nVector 2')
little_endian=43690
little_endian_to_hex(little_endian)
number_of_bytes(value)
print('Little endian:', little_endian)
# Vector 3
print('\nVector 3')
little_endian=4294967295
little_endian_to_hex(little_endian)
number_of_bytes(value)
print('Little endian:', little_endian)
# Vector 4
print('\nVector 4')
little_endian=240
little_endian_to_hex(little_endian)
number_of_bytes(value)
print('Little endian:', little_endian)
#Task 4: big endian to hex
print('\nTask 4: big endian to hex')
# Vector 1
print('\nVector 1')
big_endian=115339776388732929035197660848497720713218148788040405586178452820382218977280
big_endian_to_hex(big_endian)
number_of_bytes(value)
print('Big endian:', big_endian)
# Vector 2
print('\nVector 2')
big_endian=77193548260167611359494267807458109956502771454495792280332974934474558013440
big_endian_to_hex(big_endian)
number_of_bytes(value)
print('Big endian:', big_endian)
# Vector 3
print('\nVector 3')
big_endian=4294967295
big_endian_to_hex(big_endian)
number_of_bytes(value)
print('Big endian:', big_endian)
# Vector 4
print('\nVector 4')
big_endian=979114576324830475023518166296835358668716483481922294110218890578706788723335115795775136189060210944584475044786808910613350098299181506809283832360654948074334665509728123444088990750984735919776315636114949587227798911935355699067813766573049953903257414411690972566828795693861196044813729172123152193769005290826676049325224028303369631812105737593272002471587527915367835952474124875982077070337970837392460768423348044782340688207323630599527945406427226264695390995320400314062984891593411332752703846859640346323687201762934524222363836094053204269986087043470117703336873406636573235808683444836432453459818599293667760149123595668832133083221407128310342064668595954073131257995767262426534143159642539179485013975461689493733866106312135829807129162654188209922755829012304582671671519678313609748646814745057724363462189490278183457296449014163077506949636570237334109910914728582640301294341605533983878368789071427913184794906223657920124153256147359625549743656058746335124502376663710766611046750739680547042183503568549468592703882095207981161012224965829605768300297615939788368703353944514111011011184191740295491255291545096680705534063721012625490368756140460791685877738232879406346334603566914069127957053440
big_endian_to_hex(big_endian)
number_of_bytes(value)
print('Big endian:', big_endian)