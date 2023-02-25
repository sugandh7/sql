drop table file1_table ;
create table file1_table (field1 varchar,field2 varchar,field3 varchar,field4 varchar,field5 varchar);

select * from file1_table;

bulk insert file1_table
  from 'C:\Users\NIKHIL\Desktop\upwork_proj1\file1.csv'
  WITH
  (
  FIRSTROW = 2,
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n'


  );
  drop table file1_final;
  create table file1_final(field1 varchar,field2 varchar,field3 varchar,field4 varchar,field5 varchar,iud varchar);
  MERGE file1_final AS Target
USING file1_table	AS Source
ON (Source.field1 = Target.field1 and Source.field2 = Target.field2)
    
-- For Inserts
WHEN NOT MATCHED BY Target THEN
    INSERT VALUES (Source.field1,Source.field2,Source.field3,Source.field4,Source.field5,'I')
    
-- For Updates
WHEN MATCHED and Source.field1 = Target.field1 and Source.field2 = Target.field2 THEN 
	UPDATE SET
    Target.field3	= Source.field3,
    Target.field4		= Source.field4,
    Target.field5		= Source.field5,
	Target.iud		= 'U'
	-- For Deletes
WHEN NOT MATCHED BY Source THEN
	UPDATE SET
	Target.iud		= 'D';
select * from file1_table;

select * from file1_final;

truncate table file1_table;
select * from file1_table;
bulk insert file1_table
  from 'C:\Users\NIKHIL\Desktop\upwork_proj1\file2.csv'
  WITH
  (
  FIRSTROW = 2,
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n'
  );
  select * from file1_table;

  select * from file1_final;

  MERGE file1_final AS Target
USING file1_table	AS Source
ON (Source.field1 = Target.field1 and Source.field2 = Target.field2)
    
-- For Inserts
WHEN NOT MATCHED BY Target THEN
    INSERT VALUES (Source.field1,Source.field2,Source.field3,Source.field4,Source.field5,'I')
    
-- For Updates
WHEN MATCHED  THEN 
	UPDATE SET
    Target.field3	= Source.field3,
    Target.field4		= Source.field4,
    Target.field5		= Source.field5,
	Target.iud		= 'U'
	-- For Deletes
WHEN NOT MATCHED BY Source THEN
	UPDATE SET
	Target.iud		= 'D';
	select * from file1_final;
