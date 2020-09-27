
import pygame

class SpriteSheet:
	def __init__(self, file_name, rows_count, cols_count):
		self.sheet = pygame.image.load(file_name)
		self.rows_count = rows_count
		self.cols_count = cols_count
		self.rect = self.sheet.get_rect()
		w = self.cell_width = self.rect.width / cols_count
		h = self.cell_height = self.rect.height / rows_count
		# calc cell area
		# self.cells_areas = [ ((i%cols)*w, (i/cols)*h, w, h) for i in range(self.totalCellCount) ]
		self.cells_areas = [[ (i*h, j*w , h, w) for j in range(cols_count)] for i in range(rows_count)]
		# self.cells = []
		# for i in range(self.rows_count*self.cols_count):
		#     self.cells.append(((i%cols_count)*w, (i//cols_count)*h, w, h))    
		
	def draw(self, dest_surface, pos, cell_row=0, cell_col=0):
		dest_surface.blit(self.sheet, pos, self.cells_areas[cell_row][cell_col])
