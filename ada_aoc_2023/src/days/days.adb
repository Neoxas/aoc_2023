with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings;
with Ada.Strings.Maps;
with Days.Day_1;

package body Days is
    
    procedure Run_Day_1( Input_File: String ) is
    begin
      Put_Line( "--- Day 1 ---" );
      Day_1.Part_1(Input_File);
    end Run_Day_1;
end Days;
