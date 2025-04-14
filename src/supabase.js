import { createClient } from "@supabase/supabase-js";

const supabaseUrl = 'https://cklkhwitotdvasiwjoqk.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNrbGtod2l0b3RkdmFzaXdqb3FrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODY2NDA2NzYsImV4cCI6MjAwMjIxNjY3Nn0.-By4kxtk2m5ijhny-_JHFyXeukF8dztR2SqZ60mkWV8';

export const supabase = createClient(supabaseUrl, supabaseKey);