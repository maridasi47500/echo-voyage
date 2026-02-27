class CreateMusicalstreets < ActiveRecord::Migration[8.0]
  def change
    create_table :musicalstreets do |t|
      t.string :lieu
      t.string :lat
      t.string :lon

      t.timestamps
    end
  end
end
