with Days; use Days;
with Utilities; use Utilities;

procedure Ada_Aoc_2023 is
    Day : constant String := Get_Day;
    Filename : constant String := Get_Filename;
begin
    if Day = "1" then
        Run_Day_1(Filename);

    end if;
end Ada_Aoc_2023;
