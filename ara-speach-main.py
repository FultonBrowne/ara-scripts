'''this is the ara version of fast speach learning
    Copyright (C) 2019  Andromeda software

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''
def main():
       i=1
       while i == 1:
                print ("wecome to the very first version of the ara voice script")
                print ("please enter command or help if you need to")
                

                cmd = input()
                if (cmd == "help"):
                        print("type in start to open files at set location")
                        print("type open to start with a current data base")
                        print("type info for the boring stuff")
                elif (cmd == "info"):
                        print("this is the ara version of fast speach learning")
                        print("Copyright (C) 2019  Andromeda software")
                        print("This program is free software: you can redistribute it and/or modifyit under the terms of the GNU General Public License as published bythe Free Software Foundation, either version 3 of the License, or(at your option) any later version.")
                        print(" This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty ofMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See theGNU General Public License for more details.")
                        print("You should have received a copy of the GNU General Public Licensealong with this program.  If not, see <https://www.gnu.org/licenses/>.")
                else:
                        print("whoops please try again or type help")
                
main()
