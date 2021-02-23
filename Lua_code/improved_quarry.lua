term.clear()
term.setCursorPos(1,1)
io.write("Welcome to ruiz's quarry program!")
term.setCursorPos(1,2)
width = 10
tmpWidth = width
term.setCursorPos(1,3)
height = 3
 
coords = {gps.locate()}
posX = coords[1]
tmpPosX = posX
posY = coords[2]
posZ = coords[3]
tmpPosZ = posZ
facing = 1
valuables = {"minecraft:gold_ore","minecraft:nether_quartz","minecraft:lapis_lazuli","minecraft:coal","minecraft:iron_ore","minecraft:redstone","minecraft:coal_block","computercraft:disk_expanded","minecraft:diamond","minecraft:obsidian"}
 
function updateOrientation()
    --posX vertice is the one its facing on start--
    if facing == 1 and tmpPosX >= tmpWidth then
        facing = 2
        tmpPosX = 0
        turtle.turnRight()
    elseif facing == 2 and tmpPosZ >= tmpWidth then
        facing = 3
        tmpPosZ = 0
        turtle.turnRight()
    elseif facing == 3 and tmpPosX >= tmpWidth then
        facing = 4
        tmpPosX = 0
        turtle.turnRight()
    elseif facing == 4 and tmpPosZ >= tmpWidth - 1 then
        facing = 1
        tmpPosZ = 0
        tmpPosX = 0
        tmpWidth = tmpWidth - 1
        turtle.turnRight()
    end
end
 
function moveCheck()
    if turtle.detect() == true then
        turtle.dig()
    end
    turtle.forward()
end
 
function updatePos()
    moveCheck()
    if facing == 1 then
        tmpPosX = tmpPosX + 1
        posX = posX + 1
    elseif facing == 2 then
        tmpPosZ = tmpPosZ + 1
        posZ = posZ + 1
    elseif facing == 3 then
        tmpPosX = tmpPosX + 1
        posX = posX - 1
    elseif facing == 4 then
        tmpPosZ = tmpPosZ + 1
        posZ = posZ - 1
    end
    coords[1] = posX
    coords[3] = posZ 
    updateOrientation()
end
 
function checkLayer()
    if tmpWidth <= 1 and ((posX == 0 and posZ == 0) or (posX == width and posZ == 0) or (posX == 0 and posZ == width) or (posX == width and posZ == width)) then
        if height > 0 then
            turtle.digDown()
            turtle.down()
        end
        tmpWidth = width
        height = height - 1
        coords[2] = posY
        dumpGarbage()
    end                                       
end
                   
function dumpGarbage()
    turtle.select(1)
    for slot = 1,16 do
        if turtle.getItemDetail(slot) then
            isValuable = false
            for key, value in pairs(turtle.getItemDetail(slot)) do
                if key == "name" then
                    for key2, value2 in pairs(valuables) do
                        if value == value2 then
                           isValuable = true 
                        end
                    end
                    if isValuable == false then
                        turtle.select(slot)
                        turtle.drop()
                    end
                end
            end
        end
    end
end
 
function quarry()
    if turtle.getFuelLevel() < 2 then
        turtle.refuel()
    end
     updatePos()
     checkLayer()           
end   
 
function reproduce()
--Plant more turtles from inv
end
 
while height >= 0 do
    quarry()
    print("")
    io.write("PosX: ")
    io.write(posX)
    print("")
    io.write("tmpPosX: ")
    io.write(tmpPosX)
    print("")
    io.write("tmpWidth: ")
    io.write(tmpWidth)
end